param(
    [string]$DestinationRoot
)

$ErrorActionPreference = 'Stop'
$repositoryRoot = Split-Path -Parent $PSScriptRoot
$sourceSkill = Join-Path $repositoryRoot 'skills\production-web-standard'

if (-not $DestinationRoot) {
    $codexBase = if ($env:CODEX_HOME) {
        $env:CODEX_HOME
    } else {
        Join-Path ([Environment]::GetFolderPath('UserProfile')) '.codex'
    }
    $DestinationRoot = Join-Path $codexBase 'skills'
}

$targetSkill = Join-Path $DestinationRoot 'production-web-standard'

if (Test-Path -LiteralPath $targetSkill) {
    throw "Installation already exists at $targetSkill. Remove or back it up before reinstalling."
}

New-Item -ItemType Directory -Path $DestinationRoot -Force | Out-Null
Copy-Item -LiteralPath $sourceSkill -Destination $targetSkill -Recurse
Write-Output "Installed production-web-standard to $targetSkill"
