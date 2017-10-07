foreach($line in Get-Content .\hostnames.txt) {
    Try{
    $ResolvedIP = Resolve-DnsName -Name $line -Type A -ErrorAction Stop
    Write-Output $ResolvedIP
    }
    Catch{}
}
