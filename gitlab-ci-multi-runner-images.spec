Summary:	Prebuilt docker images for gitlab-ci-multi-runner
Name:		gitlab-ci-multi-runner-images
Version:	1.5.2
Release:	1
License:	MIT
Group:		Development/Building
Source0:	https://gitlab-ci-multi-runner-downloads.s3.amazonaws.com/master/docker/prebuilt-x86_64.tar.xz
# Source0-md5:	0d89c7578a0b5d22a4ae85dcb7d5b4f5
Source1:	https://gitlab-ci-multi-runner-downloads.s3.amazonaws.com/master/docker/prebuilt-arm.tar.xz
# Source1-md5:	c0533c581624dcb33095f08f06e6a00b
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
