foreach($line in Get-Content .\wordlist.txt) {
    Try{
    $subdomain = "$line.$args"
    $ResolvedIP = Resolve-DnsName -Name $subdomain -Type A -ErrorAction Stop
    Write-Output $ResolvedIP
    }
    Catch{}
}
