import os
import pip
import pkg_resources

# Function to get the size of a directory
def get_size(start_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

# List all installed packages
installed_packages = {pkg.key: pkg for pkg in pkg_resources.working_set}

# Print package name and size
for package_name in installed_packages:
    package_location = installed_packages[package_name].location
    package_size = get_size(package_location)
    print(f"{package_name}: {package_size / (1024 ** 2):.2f} MB")
