
# Step 3: Set up Python virtual environment
$venvDir = Join-Path $PSScriptRoot "venv"
if (-not (Test-Path $venvDir)) {
    python -m venv $venvDir
}

# Step 4: Install packages from packages.txt using the venv
$packagesFile = Join-Path $PSScriptRoot "packages.txt"
if (Test-Path $packagesFile) {
    $activateScript = Join-Path $venvDir "Scripts\Activate.ps1"
    if (Test-Path $activateScript) {
        . $activateScript
        pip install -r $packagesFile
        deactivate
    } else {
        Write-Host "Activate script not found in venv directory."
    }
} else {
    Write-Host "packages.txt not found."
}
