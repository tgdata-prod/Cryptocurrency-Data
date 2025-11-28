function Load-DotEnv {
    param (
        [string]$Path = ".env"
    )

    if (-Not (Test-Path $Path)) {
        Write-Warning "No .env file found at path '$Path'"
        return
    }

    Get-Content $Path | ForEach-Object {
        # Skip comments and blank lines
        if ($_ -match "^\s*#" -or [string]::IsNullOrWhiteSpace($_)) {
            return
        }

        if ($_ -match "^\s*([^=]+?)\s*=\s*(.*)$") {
            $key = $matches[1].Trim()
            $value = $matches[2].Trim('"')
            [System.Environment]::SetEnvironmentVariable($key, $value, "Process")
        }
    }
}
