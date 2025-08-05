{ pkgs }: {
  deps = [
    pkgs.python311
    pkgs.python311Packages.pandas
    pkgs.python311Packages.matplotlib
    pkgs.python311Packages.seaborn
    pkgs.python311Packages.numpy
  ];
}