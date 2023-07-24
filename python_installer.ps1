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
    $pythonInstallerUrl = "https://www.python.org/ftp/python/3.11.4/python-3.11.4-amd64.exe"
    $pythonInstallerPath = Join-Path $PSScriptRoot "python-3.11.4-amd64.exe"

    Invoke-WebRequest -Uri $pythonInstallerUrl -OutFile $pythonInstallerPath
    Start-Process -FilePath $pythonInstallerPath -ArgumentList "/passive InstallAllUsers=1 PrependPath=1" -Wait
    Write-Host "Downloaded Python 3.11.4"
}

Start-Sleep -Seconds 2
$scriptDir = Join-Path $PSScriptRoot "install_package.ps1"
Start-Process powershell.exe -ArgumentList "-ExecutionPolicy Bypass -File '$scriptDir'" -Wait