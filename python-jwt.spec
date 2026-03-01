Name:		python-jwt
Version:	1.4.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/j/jwt/jwt-%{version}.tar.gz
Summary:	JSON Web Token library for Python 3.
URL:		https://pypi.org/project/jwt/
License:	None
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
JSON Web Token library for Python 3.

%files
%{py_sitedir}/jwt
%{py_sitedir}/jwt-*.*-info
