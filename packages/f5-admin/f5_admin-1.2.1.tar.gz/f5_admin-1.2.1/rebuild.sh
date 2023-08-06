#!/bin/sh
# build and installation script
cd /Users/sli/f5-admin
# source venv/bin/activate
python setup.py clean
rm -rf build
python setup.py sdist bdist_wheel
sudo pip uninstall f5-admin
sudo pip install dist/f5_admin-1.2.0.tar.gz
#ln -s /Library/Python/2.7/site-packages/f5_admin/conf/ ./conf
