Summary:	Prebuilt docker images for gitlab-ci-multi-runner
Name:		gitlab-ci-multi-runner-images
Version:	9.5.0
Release:	2
License:	MIT
Group:		Development/Building
Source0:	http://gitlab-ci-multi-runner-downloads.s3.amazonaws.com/v%{version}/docker/prebuilt-x86_64.tar.xz
# Source0-md5:	3e17865359e937955302f73752426cd4
Source1:	http://gitlab-ci-multi-runner-downloads.s3.amazonaws.com/v%{version}/docker/prebuilt-arm.tar.xz
# Source1-md5:	3e566c807f5d9ad654a29e133b3f683d
URL:		https://gitlab.com/gitlab-org/gitlab-ci-multi-runner/tree/master/dockerfiles/build
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		imgdir	/var/lib/gitlab-runner

%description
Prebuilt docker images for gitlab-ci-multi-runner.

%package -n gitlab-ci-multi-runner-image-arm
Summary:	Prebuilt arm docker image for gitlab-ci-multi-runner
Group:		Development/Building

%description -n gitlab-ci-multi-runner-image-arm
Prebuilt arm docker image for gitlab-ci-multi-runner.

%package -n gitlab-ci-multi-runner-image-x86_64
Summary:	Prebuilt arm docker image for gitlab-ci-multi-runner
Group:		Development/Building

%description -n gitlab-ci-multi-runner-image-x86_64
Prebuilt arm docker image for gitlab-ci-multi-runner.

%prep
%setup -qcT

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{imgdir}

cp -p %{SOURCE0} $RPM_BUILD_ROOT%{imgdir}
cp -p %{SOURCE1} $RPM_BUILD_ROOT%{imgdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files -n gitlab-ci-multi-runner-image-arm
%defattr(644,root,root,755)
%{imgdir}/prebuilt-arm.tar.xz

%files -n gitlab-ci-multi-runner-image-x86_64
%defattr(644,root,root,755)
%{imgdir}/prebuilt-x86_64.tar.xz
