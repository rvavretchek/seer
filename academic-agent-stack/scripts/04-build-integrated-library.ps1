@param([switch]$Clean)
$ErrorActionPreference="Stop"
$a=@(".\scripts\04-build-integrated-library.py");if($Clean){$a+="--clean"};python @a
