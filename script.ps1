# Function to check Python version
function Get-PythonVersion {
    $pythonVersion = (python --version 2>&1)
    if ($LASTEXITCODE -ne 0) {
        return $null
    }

    $versionString = $pythonVersion.Trim().Split(' ')[1]
    $major = [int]$versionString.Split('.')[0]
    $minor = [int]$versionString.Split('.')[1]

    return "$major.$minor"
}

# Step 1: Check Python version
$requiredPythonVersion = "3.11"
$installedPythonVersion = Get-PythonVersion

if ($null -eq $installedPythonVersion -or $installedPythonVersion -lt $requiredPythonVersion) {
    # Step 2: Install Python 3.11 or the latest version
    $pythonInstallerUrl = "https://www.python.org/ftp/python/3.11.7/python-3.11.7-amd64.exe"
    $pythonInstallerPath = Join-Path $PSScriptRoot "python-3.11.7-amd64.exe"

    Invoke-WebRequest -Uri $pythonInstallerUrl -OutFile $pythonInstallerPath
    Start-Process -FilePath $pythonInstallerPath -ArgumentList "/passive InstallAllUsers=1 PrependPath=1" -Wait
    Write-Host "Downloaded Python"
    Start-Sleep -Seconds 1
    $env:Path=([System.Environment]::GetEnvironmentVariable("Path","Machine"),[System.Environment]::GetEnvironmentVariable("Path","User")) -match '.' -join ';'
    # After installation, recheck Python version
    $installedPythonVersion = Get-PythonVersion
}

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
