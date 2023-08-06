"""Module for general utilities."""

# stdlib
import copy
import logging
import os
import re
from dataclasses import dataclass
from enum import Enum
from glob import glob
from pathlib import PosixPath
from typing import Union, Optional, Dict, List

# tdub
import tdub.constants

log = logging.getLogger(__name__)

FileLike = Union[str, os.PathLike]
PathLike = Union[str, os.PathLike]
FileOrFiles = Union[List[FileLike], FileLike]
PathOrPaths = Union[List[PathLike], PathLike]


class Region(Enum):
    """A simple enum class for easily using region information.

    Attributes
    ----------
    r1j1b
       A label for our ``1j1b`` region.
    r2j1b
       A label for our ``2j1b`` region.
    r2j2b = 1
       A label for our ``2j2b`` region.

    Examples
    --------
    Using this enum for grabing the ``2j2b`` region from a set of
    files:

    >>> from tdub.utils import Region
    >>> from tdub.branches import get_selection
    >>> from tdub.frames import iterative_selection
    >>> df = iterative_selection(files, get_selection(Region.r2j2b))
    """

    r1j1b = 0
    r2j1b = 1
    r2j2b = 2
    rUnkn = 9

    @staticmethod
    def from_str(s: str) -> "Region":
        """Get enum value for the given string.

        This function supports three ways to define a region; prefixed
        with "r", prefixed with "reg", or no prefix at all. For
        example, ``Region.r2j2b`` can be retrieved like so:

        - ``Region.from_str("r2j2b")``
        - ``Region.from_str("reg2j2b")``
        - ``Region.from_str("2j2b")``

        Parameters
        ----------
        s : str
           string representation of the desired region

        Returns
        -------
        Region
           the enum version

        Examples
        --------
        >>> from tdub.utils import Region
        >>> Region.from_str("1j1b")
        <Region.r1j1b: 0>
        """
        if s.startswith("reg"):
            rsuff = s.split("reg")[-1]
            return Region.from_str(rsuff)
        elif s.startswith("r"):
            return Region[s]
        else:
            if s == "2j2b":
                return Region.r2j2b
            elif s == "2j1b":
                return Region.r2j1b
            elif s == "1j1b":
                return Region.r1j1b
            else:
                raise ValueError(f"{s} doesn't correspond to a Region")

    def __str__(self) -> str:
        return self.name[1:]


@dataclass
class SampleInfo:
    """Describes a sample's attritubes given it's name.

    Parameters
    ----------
    input_file : str
       the file stem containing the necessary groups to parse

    Attributes
    ----------
    phy_process : str
       physics process (e.g. ttbar or tW_DR or Zjets)
    dsid : int
       the dataset ID
    sim_type : str
       the simulation type, "FS" or "AFII"
    campaign : str
       the campaign, MC16{a,d,e}
    tree : str
       the original tree (e.g. "nominal" or "EG_SCALE_ALL__1up")

    Examples
    --------
    >>> from tdub.utils import SampleInfo
    >>> sampinfo = SampleInfo("ttbar_410472_AFII_MC16d_nominal.root")
    >>> sampinfo.phy_process
    ttbar
    >>> sampinfo.dsid
    410472
    >>> sampinfo.sim_type
    AFII
    >>> sampinfo.campaign
    MC16d
    >>> sampinfo.tree
    nominal
    """

    phy_process: str
    dsid: int
    sim_type: str
    campaign: str
    tree: str

    _sample_info_extract_re = re.compile(
        r"""(?P<phy_process>\w+)_
        (?P<dsid>[0-9]{6})_
        (?P<sim_type>(FS|AFII))_
        (?P<campaign>MC16(a|d|e))_
        (?P<tree>\w+)
        (\.\w+|$)""",
        re.X,
    )

    def __init__(self, input_file: str) -> None:
        if "Data_Data" in input_file:
            self.phy_process = "Data"
            self.dsid = 0
            self.sim_type = "Data"
            self.campaign = "Data"
            self.tree = "nominal"
        else:
            m = self._sample_info_extract_re.match(input_file)
            if not m:
                raise ValueError(f"{input_file} cannot be parsed by SampleInfo regex")
            self.phy_process = m.group("phy_process")
            if self.phy_process.startswith("MCNP"):
                self.phy_process = "MCNP"
            self.dsid = int(m.group("dsid"))
            self.sim_type = m.group("sim_type")
            self.campaign = m.group("campaign")
            self.tree = m.group("tree")


def quick_files(datapath: FileLike, campaign: Optional[str] = None) -> Dict[str, List[str]]:
    """Get a dictionary of ``{sample_str : file_list}`` for quick file access.

    The lists of files are sorted alphabetically. These types of
    samples are currently tested:

    - `ttbar` (410472 full sim)
    - `ttbar_AFII` (410472 fast sim)
    - `ttbar_PS` (410558 fast sim)
    - `ttbar_hdamp` (410482 fast sim)
    - `ttbar_inc` (410470 full sim)
    - `ttbar_inc_AFII` (410470 fast sim)
    - `tW_DR` (410648, 410649 full sim)
    - `tW_DR_AFII` (410648, 410648 fast sim)
    - `tW_DR_PS` (411038, 411039 fast sim)
    - `tW_DR_inc` (410646, 410647 full sim)
    - `tW_DR_inc_AFII` (410646, 410647 fast sim)
    - `tW_DS` (410656, 410657 full sim)
    - `tW_DS_inc` (410654, 410655 ful sim)
    - `Diboson`
    - `Zjets`
    - `MCNP`
    - `Data`

    Parameters
    ----------
    datapath : str or os.PathLike
       path where all of the ROOT files live
    campaign : str, optional
       enforce a single campaign ("MC16a", "MC16d", or "MC16e")

    Returns
    -------
    dict(str, list(str))
       dictionary for quick file access

    Examples
    --------
    >>> from pprint import pprint
    >>> from tdub.utils import quick_files
    >>> qf = quick_files("/path/to/some_files") ## has 410472 ttbar samples
    >>> pprint(qf["ttbar"])
    ['/path/to/some/files/ttbar_410472_FS_MC16a_nominal.root',
     '/path/to/some/files/ttbar_410472_FS_MC16d_nominal.root',
     '/path/to/some/files/ttbar_410472_FS_MC16e_nominal.root']
    >>> qf = quick_files("/path/to/some/files", campaign="MC16d")
    >>> pprint(qf["tW_DR"])
    ['/path/to/some/files/tW_DR_410648_FS_MC16d_nominal.root',
     '/path/to/some/files/tW_DR_410649_FS_MC16d_nominal.root']
    >>> qf = quick_files("/path/to/some/files", campaign="MC16a")
    >>> pprint(qf["Data"])
    ['/path/to/some/files/Data15_data15_Data_Data_nominal.root',
     '/path/to/some/files/Data16_data16_Data_Data_nominal.root']

    """
    if campaign is None:
        camp = ""
    else:
        if campaign not in ("MC16a", "MC16d", "MC16e"):
            raise ValueError(f"{campaign} but be either 'MC16a', 'MC16d', or 'MC16e'")
        camp = f"_{campaign}"

    path = str(PosixPath(datapath).resolve())

    # ttbar
    ttbar_files = sorted(glob(f"{path}/ttbar_410472_FS{camp}*nominal.root"))
    ttbar_AFII_files = sorted(glob(f"{path}/ttbar_410472_AFII{camp}*nominal.root"))
    ttbar_PS_files = sorted(glob(f"{path}/ttbar_410558*AFII{camp}*nominal.root"))
    ttbar_hdamp_files = sorted(glob(f"{path}/ttbar_410482_AFII{camp}*nominal.root"))
    ttbar_inc_files = sorted(glob(f"{path}/ttbar_410470_FS{camp}*nominal.root"))
    ttbar_inc_AFII_files = sorted(glob(f"{path}/ttbar_410470_AFII{camp}*nominal.root"))

    # tW
    tW_DR_files = sorted(
        glob(f"{path}/tW_DR_410648_FS{camp}*nominal.root")
        + glob(f"{path}/tW_DR_410649_FS{camp}*nominal.root")
    )
    tW_DR_AFII_files = sorted(
        glob(f"{path}/tW_DR_410648_AFII{camp}*nominal.root")
        + glob(f"{path}/tW_DR_410649_AFII{camp}*nominal.root")
    )
    tW_DR_inc_files = sorted(
        glob(f"{path}/tW_DR_410646_FS{camp}*nominal.root")
        + glob(f"{path}/tW_DR_410647_FS{camp}*nominal.root")
    )
    tW_DR_inc_AFII_files = sorted(
        glob(f"{path}/tW_DR_410646_AFII{camp}*nominal.root")
        + glob(f"{path}/tW_DR_410647_AFII{camp}*nominal.root")
    )
    tW_DR_PS_files = sorted(
        glob(f"{path}/tW_DR_411038_AFII{camp}*nominal.root")
        + glob(f"{path}/tW_DR_411039_AFII{camp}*nominal.root")
    )
    tW_DS_files = sorted(
        glob(f"{path}/tW_DS_410656_FS{camp}*nominal.root")
        + glob(f"{path}/tW_DS_410657_FS{camp}*nominal.root")
    )
    tW_DS_inc_files = sorted(
        glob(f"{path}/tW_DS_410654_FS{camp}*nominal.root")
        + glob(f"{path}/tW_DS_410655_FS{camp}*nominal.root")
    )

    # Minor backgrounds
    Diboson_files = sorted(glob(f"{path}/Diboson_*FS{camp}*nominal.root"))
    Zjets_files = sorted(glob(f"{path}/Zjets_*FS{camp}*nominal.root"))
    MCNP_files = sorted(glob(f"{path}/MCNP_*FS{camp}*nominal.root"))

    if campaign is None:
        Data_files = sorted(glob(f"{path}/*Data_Data_nominal.root"))
    elif campaign == "MC16a":
        Data_files = sorted(
            glob(f"{path}/Data15_data15*root") + glob(f"{path}/Data16_data16*root")
        )
    elif campaign == "MC16d":
        Data_files = sorted(glob(f"{path}/Data17_data17*root"))
    elif campaign == "MC16e":
        Data_files = sorted(glob(f"{path}/Data18_data18*root"))

    file_lists = {
        "ttbar": ttbar_files,
        "ttbar_AFII": ttbar_AFII_files,
        "ttbar_PS": ttbar_PS_files,
        "ttbar_hdamp": ttbar_hdamp_files,
        "ttbar_inc": ttbar_inc_files,
        "ttbar_inc_AFII": ttbar_inc_AFII_files,
        "tW_DR": tW_DR_files,
        "tW_DR_AFII": tW_DR_AFII_files,
        "tW_DR_PS": tW_DR_PS_files,
        "tW_DR_inc": tW_DR_inc_files,
        "tW_DR_inc_AFII": tW_DR_inc_AFII_files,
        "tW_DS": tW_DS_files,
        "tW_DS_inc": tW_DS_inc_files,
        "Diboson": Diboson_files,
        "Zjets": Zjets_files,
        "MCNP": MCNP_files,
        "Data": Data_files,
    }
    for k, v in file_lists.items():
        if len(v) == 0:
            log.debug(f"we didn't find any files for {k}")
    return file_lists


def files_for_tree(
    datapath: FileLike, sample_prefix: str, tree_name: str, campaign: Optional[str] = None,
) -> List[str]:
    """Get a list of files for the sample and desired tree.

    Parameters
    ----------
    datapath : str or os.PathLike
       path where all of the ROOT files live
    sample_prefix : str
       the prefix for the sample we want (`"ttbar"` or `"tW_DR"` or `"tW_DS"`)
    tree_name : str
       the name of the ATLAS systematic tree (e.g. `"nominal"` or `"EG_RESOLUTION_ALL__1up"`)
    campaign : str, optional
       enforce a single campaign ("MC16a", "MC16d", or "MC16e")

    Returns
    -------
    list(str)
       the list of desired files (if they exist)

    Examples
    --------
    >>> from tdub.utils import files_for_tree
    >>> files_for_tree("/data/path", "ttbar", "JET_CategoryReduction_JET_JER_EffectiveNP_4__1up")
    ['/data/path/ttbar_410472_FS_MC16a_JET_CategoryReduction_JET_JER_EffectiveNP_4__1up.root',
     '/data/path/ttbar_410472_FS_MC16d_JET_CategoryReduction_JET_JER_EffectiveNP_4__1up.root',
     '/data/path/ttbar_410472_FS_MC16e_JET_CategoryReduction_JET_JER_EffectiveNP_4__1up.root']
    """
    if campaign is None:
        camp = ""
    else:
        if campaign not in ("MC16a", "MC16d", "MC16e"):
            raise ValueError(f"{campaign} but be either 'MC16a', 'MC16d', or 'MC16e'")
        camp = f"_{campaign}"

    path = str(PosixPath(datapath).resolve())
    if sample_prefix == "ttbar":
        return sorted(glob(f"{path}/ttbar_410472_FS{camp}*{tree_name}.root"))
    elif sample_prefix == "tW_DR":
        return sorted(glob(f"{path}/tW_DR_41064*FS{camp}*{tree_name}.root"))
    elif sample_prefix == "tW_DS":
        return sorted(glob(f"{path}/tW_DS_41065*FS{camp}*{tree_name}.root"))
    else:
        raise ValueError(
            f"bad sample_prefix '{sample_prefix}', must be one of: ['tW_DR', 'tW_DS', 'ttbar']"
        )


def get_avoids(region: Union[str, Region]) -> List[str]:
    """Get the features to avoid for the given region.

    See the tdub.constants module for defintion of the variables to
    avoid. See :py:func:`tdub.utils.Region.from_str` for the
    compatible strings.

    Parameters
    ----------
    region : str or tdub.utils.Region
       the region as a string or enum entry

    Returns
    -------
    list(str)
       the list of features to avoid for the region

    Examples
    --------
    >>> from tdub.utils import get_avoids, Region
    >>> get_avoids(Region.r2j1b)
    ['HT_jet1jet2', 'deltaR_lep1lep2_jet1jet2met', 'mass_lep2jet1', 'pT_jet2']
    >>> get_avoids("2j2b")
    ['deltaR_jet1_jet2']
    """
    options = {
        Region.r1j1b: tdub.constants.AVOID_IN_CLF_1j1b,
        Region.r2j1b: tdub.constants.AVOID_IN_CLF_2j1b,
        Region.r2j2b: tdub.constants.AVOID_IN_CLF_2j2b,
    }
    if isinstance(region, str):
        return options[Region.from_str(region)]
    return options[region]


def get_features(region: Union[str, Region]) -> List[str]:
    """Get the feature list for a region.

    See the tdub.constants module for the defition of the feature
    lists. See :py:func:`tdub.utils.Region.from_str` for the
    compatible strings.

    Parameters
    ----------
    region : str or tdub.utils.Region
       the region as a string or enum entry. If ``"ALL"`` returns a
       set of unique features from all regions

    Returns
    -------
    list(str)
       the list of features for that region

    Examples
    --------
    >>> from pprint import pprint
    >>> from tdub.utils import get_features
    >>> pprint(get_features("reg2j1b"))
    ['mass_lep1jet1',
     'mass_lep1jet2',
     'mass_lep2jet1',
     'mass_lep2jet2',
     'pT_jet2',
     'pTsys_lep1lep2jet1jet2met',
     'psuedoContTagBin_jet1',
     'psuedoContTagBin_jet2']
    """
    # first allow retrieval of all features
    if region == "ALL":
        return sorted(
            set(tdub.constants.FEATURESET_1j1b)
            | set(tdub.constants.FEATURESET_2j1b)
            | set(tdub.constants.FEATURESET_2j2b),
            key=str.lower,
        )

    # if not "ALL" grab from a dict constructed from constants
    options = {
        Region.r1j1b: tdub.constants.FEATURESET_1j1b,
        Region.r2j1b: tdub.constants.FEATURESET_2j1b,
        Region.r2j2b: tdub.constants.FEATURESET_2j2b,
    }
    if isinstance(region, str):
        return options[Region.from_str(region)]
    return options[region]


def augment_features(region: Union[str, Region], to_add: List[str]) -> None:
    """Add some features to the existing lists.

    See the tdub.constants module for the defition of the feature
    lists. See :py:func:`tdub.utils.Region.from_str` for the
    compatible strings.

    Parameters
    ----------
    region : str or tdub.utils.Region
       the region as a string or enum entry
    to_add : list(str)
       the new features to add

    Examples
    --------
    >>> from tdub.utils import augment_features, get_features
    >>> "another" in get_features("2j2b")
    False
    >>> "feature" in get_features("2j2b")
    False
    >>> augment_features("2j2b", ["another", "feature"])
    >>> "another" in get_features("2j2b")
    True
    >>> "feature" in get_features("2j2b")
    True
    """
    if isinstance(region, str):
        region = Region.from_str(region)
    if region == Region.r1j1b:
        tdub.constants.FEATURESET_1j1b += to_add
    elif region == Region.r2j1b:
        tdub.constants.FEATURESET_2j1b += to_add
    elif region == Region.r2j2b:
        tdub.constants.FEATURESET_2j2b += to_add
    else:
        raise ValueError("Bad region value")


def override_features(table: Dict[str, List[str]]) -> None:
    """Programacically override feature lists in tdub.constants module.

    Given a dictionary of the form

    .. code-block:: python

        overrides = {
            "r1j1b": ["new1", "new2", "new3"],
            "r2j1b": ["new1", "new2", "new3", "new4"],
            "r2j2b": ["new1", "new2"],
        }

    we override the module constants:

    - :py:data:`tdub.constants.FEATURESET_1j1b`
    - :py:data:`tdub.constants.FEATURESET_2j1b`
    - :py:data:`tdub.constants.FEATURESET_2j2b`

    Note
    ----

    Not all regions need to be defined; only those you wish to
    override.

    Parameters
    ----------
    table : dict(str, list(str))
       region to feature list table

    Examples
    --------
    Using the dictionary above as an example

    >>> from tdub.utils import override_features, get_features
    >>> import tdub.constants
    >>> tdub.constants.FEATURESET_1j1b
    ["old1", "old2"]
    >>> get_features("1j1b")
    ["old1", "old2"]
    >>> override_features(overrides)
    >>> get_features("1j1b")
    ["new1", "new2", "new3"]
    >>> tdub.constants.FEATURESET_1j1b
    ["new1", "new2", "new3"]
    """
    if "r1j1b" in table:
        log.info("Overriding tdub.constants.FEATURESET_1j1b")
        tdub.constants.FEATURESET_1j1b = copy.deepcopy(table["r1j1b"])
    if "r2j1b" in table:
        log.info("Overriding tdub.constants.FEATURESET_2j1b")
        tdub.constants.FEATURESET_2j1b = copy.deepcopy(table["r2j1b"])
    if "r2j2b" in table:
        log.info("Overriding tdub.constants.FEATURESET_2j2b")
        tdub.constants.FEATURESET_2j2b = copy.deepcopy(table["r2j2b"])
