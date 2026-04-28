<#
.SYNOPSIS
    Set-FullControl
    PowerShell Function: Set-FullControl
    Author: Nithin
.EXAMPLE
    Set-FullControl -user domain\igris -path C:\Users\Administrator
#>
function Set-FullControl {
    param (
        [string]$user,
        [string]$path
    )
    if (-not $user -or -not $path) {
        Get-Help Set-FullControl
        return
    }
    if (-not (Test-Path $path)) {
        Write-Host "[-] Path not found: $path" -ForegroundColor Red
        return
    }
    "[+] Current permissions:"
    Get-Acl $path | Format-List
    "[+] Changing permissions on: $path"
    $acl = Get-Acl $path
    $aclpermisos = $user, 'FullControl', 'ContainerInherit,ObjectInherit', 'None', 'Allow'
    $permisoacl = New-Object System.Security.AccessControl.FileSystemAccessRule $aclpermisos
    $acl.AddAccessRule($permisoacl)
    Set-Acl -Path $path -AclObject $acl
    "[+] ACLs changed successfully."
    Get-Acl -Path $path | Format-List
}
