Name:           ros-indigo-prace-gripper-driver
Version:        0.6.0
Release:        0%{?dist}
Summary:        ROS prace_gripper_driver package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/prace_gripper_driver
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  ros-indigo-catkin

%description
prace_gripper_driver

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Wed Sep 17 2014 Alexander Bubeck <aub@ipa.fhg.de> - 0.6.0-0
- Autogenerated by Bloom

* Mon Aug 25 2014 Alexander Bubeck <aub@ipa.fhg.de> - 0.5.2-0
- Autogenerated by Bloom

