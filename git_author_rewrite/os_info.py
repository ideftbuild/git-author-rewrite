# #!/usr/bin/python3
# from platform import system
# # import platform
# from distro import id
#
#
#
# def get_package_manager(os_id):
#     package_managers = {
#         "arch": "pacman",
#         "ubuntu": "apt",
#         "debian": "apt",
#         "fedora": "dnf",
#         "centos": "yum",
#         "opensuse": "zypper",
#         "alpine": "apk"
#     }
#     return package_managers.get(os_id, 'unknown')
#     
#
# def get_os_info():
#
#     os = system()
#
#     print("OS: " + os)
#     if os == 'Linux':
#         os_id = id()
#         return { 'name': os_id, 'pkg_manager': get_package_manager(os_id) }
#     elif os == 'Windows':
#         return { 'name': 'windows' }
#     elif os == 'Darwin':
#         return { 'name': 'mac' }
#     else:
#         return None
#
