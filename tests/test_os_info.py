# #!/usr/bin/env python3 
#
# import pytest
# from unittest import mock
# from git_author_rewrite.os_info import get_os_info, get_package_manager
#
#
# def test_get_os_info_Ubuntu():
#     
#     with mock.patch('git_author_rewrite.os_info.system', return_value='Linux'), \
#         mock.patch('git_author_rewrite.os_info.id', return_value='ubuntu'):
#         os_info = get_os_info()
#
#         assert isinstance(os_info, dict), f'Expected obj to be a dictionary, but got {type(os_info)}'
#         assert os_info.get("name") == 'ubuntu'
#
# def test_get_os_info_Arch():
#     
#     os_info = get_os_info()
#
#     print("Dictionary contains: ", os_info)
#     assert isinstance(os_info, dict), f'Expected obj to be a dictionary, but got {type(os_info)}'
#     assert os_info.get("name") == 'arch'
#
#
# def test_get_os_info_Windows():
#     
#     with mock.patch('git_author_rewrite.os_info.system', return_value='Windows'):
#         os_info = get_os_info()
#
#         assert isinstance(os_info, dict), f'Expected obj to be a dictionary, but got {type(os_info)}'
#         assert os_info.get("name") == 'windows'
#
#
# def test_get_os_info_MacOS():
#     with mock.patch('git_author_rewrite.os_info.system', return_value='Darwin'):
#         os_info = get_os_info()
#
#         assert isinstance(os_info, dict), f'Expected obj to be a dictionary, but got {type(os_info)}'
#         assert os_info.get("name") == 'mac'
#
#
# def test_get_package_manager():
#     assert get_package_manager("arch") == "pacman"
#     assert get_package_manager("ubuntu") == "apt"
#     assert get_package_manager("debian") == "apt"
#     assert get_package_manager("fedora") == "dnf"
#     assert get_package_manager("centos") == "yum"
#     assert get_package_manager("opensuse") == "zypper"
#     assert get_package_manager("alpine") == "apk"
#     assert get_package_manager("not a package manager") == "unknown"
