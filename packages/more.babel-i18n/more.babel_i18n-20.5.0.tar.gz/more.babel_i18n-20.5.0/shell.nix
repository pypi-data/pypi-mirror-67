{ usePipenvShell ? false }:
let
  pkgs = import <nixpkgs> {};
  lib = pkgs.lib;
  envVars = ''
    export GIT_SSL_CAINFO="${pkgs.cacert}/etc/ssl/certs/ca-bundle.crt"; 
  '';

in pkgs.stdenv.mkDerivation {
  src = null;
  name = "more-babel-i18n-dev-env";
  phases = [];
  propagatedBuildInputs = with pkgs; [ 
    cacert
    entr
    pipenv
    zsh
  ] ++
  (with python38Packages; [
    autopep8
    ipdb
    mypy
    pylint
    python 
    setuptools_scm
    twine
    wheel
  ]);
  shellHook = envVars + (lib.optionalString 
                         usePipenvShell "SHELL=`which zsh` exec pipenv shell --fancy");
}
