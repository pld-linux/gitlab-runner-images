Summary:	Prebuilt docker images for gitlab-runner
Name:		gitlab-runner-images
Version:	10.2.0
Release:	1
License:	MIT
Group:		Development/Building
Source0:	http://gitlab-runner-downloads.s3.amazonaws.com/v%{version}/docker/prebuilt-x86_64.tar.xz
# Source0-md5:	ada4fed13edd764fc66f286246b89cbe
Source1:	http://gitlab-runner-downloads.s3.amazonaws.com/v%{version}/docker/prebuilt-arm.tar.xz
# Source1-md5:	17c4e694df6b0b8a0a12f9b027f337fb
URL:		https://gitlab.com/gitlab-org/gitlab-runner/tree/master/dockerfiles/build
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		imgdir	/var/lib/gitlab-runner

%description
Prebuilt docker images for gitlab-runner.

%package -n gitlab-runner-image-arm
Summary:	Prebuilt arm docker image for gitlab-runner
Group:		Development/Building
Obsoletes:	gitlab-ci-multi-runner-image-arm < 10.0

%description -n gitlab-runner-image-arm
Prebuilt arm docker image for gitlab-runner.

%package -n gitlab-runner-image-x86_64
Summary:	Prebuilt arm docker image for gitlab-runner
Group:		Development/Building
Obsoletes:	gitlab-ci-multi-runner-image-x86_64 < 10.0

%description -n gitlab-runner-image-x86_64
Prebuilt arm docker image for gitlab-runner.

%prep
%setup -qcT

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{imgdir}

cp -p %{SOURCE0} $RPM_BUILD_ROOT%{imgdir}
cp -p %{SOURCE1} $RPM_BUILD_ROOT%{imgdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files -n gitlab-runner-image-arm
%defattr(644,root,root,755)
%{imgdir}/prebuilt-arm.tar.xz

%files -n gitlab-runner-image-x86_64
%defattr(644,root,root,755)
%{imgdir}/prebuilt-x86_64.tar.xz
