import re

from solcx import install_solc_pragma, set_solc_version_pragma, compile_source
from solcx.exceptions import SolcError, UnsupportedVersionError

pragma_pattern = re.compile(
    r'^\s*pragma\s+solidity\s+.*?;',
    re.MULTILINE
)

import_pattern = re.compile(
    r'^\s*import\s+(?:"([^"]+)"|\'([^\']+)\'|{[^}]+}\s+from\s+["\']([^"\']+)["\']|[\w\d./_-]+)\s*;',
    re.MULTILINE
)

class ExternalInclusionError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class VersionNotFoundError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def get_version(source):
    include = import_pattern.search(source)
    if include:
        raise ExternalInclusionError("File contains external libraries")
    version = pragma_pattern.search(source)
    if not version:
        raise VersionNotFoundError("Cannot define file version")
    return version.group(0)

def sol_components(source):
    try:
        result = {}
        version = get_version(source)
        install_solc_pragma(version)
        v = set_solc_version_pragma(version)

        compiled_sol = compile_source(
            source,
            output_values=["opcodes"],
            optimize=True,
            optimize_runs=200,
        )

        for name, opcodes in compiled_sol.items():
            contract_name = name.split(':')[-1]
            result[contract_name] = opcodes['opcodes']

        return v, result
    except ExternalInclusionError as e:
        print(e.message)
        return None
    except VersionNotFoundError as e:
        print(e.message)
        return None
    except SolcError as e:
        print(e.message)
        return None
    except UnsupportedVersionError:
        return None

def package_assemble(source):
    version, opcodes = sol_components(source)
    package = {
        'compiler-version': str(version),
        'contracts': opcodes
    }
    return package