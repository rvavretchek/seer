@param([switch]$IncludeLarge,[switch]$Force)
$ErrorActionPreference="Stop"
$a=@(".\scripts\01-download-libraries.py");if($IncludeLarge){$a+="--include-large"};if($Force){$a+="--force"};python @a
