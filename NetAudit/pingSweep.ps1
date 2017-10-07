#Takes in arguments x.x.x.x-y.y.y.y OR z.z.z.z/w
$ipStart, $ipEnd = $args.Split("-")
if (-Not ($ipEnd)) {
    $ipStart, $cidr = $args.Split("/")
}
#get the octet
$startFirst, $startSecond, $startThird, $startFourth = $ipStart.Split(".")

if ($cidr) {

    if (($cidr -eq 24) -Or ($cidr -eq 16) -Or ($cidr -eq 8)){$octet = 255}
    elseif (($cidr -eq 23) -Or ($cidr -eq 15) -Or ($cidr -eq 7)){$octet = 254}
    elseif (($cidr -eq 22) -Or ($cidr -eq 14) -Or ($cidr -eq 6)){$octet = 252}
    elseif (($cidr -eq 21) -Or ($cidr -eq 13) -Or ($cidr -eq 5)){$octet = 248}
    elseif (($cidr -eq 20) -Or ($cidr -eq 12) -Or ($cidr -eq 4)){$octet = 240}
    elseif (($cidr -eq 19) -Or ($cidr -eq 11) -Or ($cidr -eq 3)){$octet = 224}
    elseif (($cidr -eq 18) -Or ($cidr -eq 10) -Or ($cidr -eq 2)){$octet = 192}
    elseif (($cidr -eq 17) -Or ($cidr -eq 9) -Or ($cidr -eq 1)){$octet = 128}

if ($cidr -gt 16 -and $cidr -le 24)
{
    Write-Output "cidr le 24= $cidr"
    for ($endFourth = 0; $endFourth -lt $octet; $endFourth++) {
        $scan = $startFirst + "." + $startSecond + "." + $startThird + "." + $endFourth
        Write-Output "Pinging $scan"
        if ( Test-Connection $scan -count 1 -quiet) {
            Write-Output "$scan is online!"
        }
    }

}
if ($cidr -gt 8 -and $cidr -le 16)
{
            Write-Output "cidr le 16= $cidr"
            for ($thirdOctet = $startThird; $thirdOctet -lt $octet; $thirdOctet++) {
                for ($fourthOctet = 0; $fourthOctet -lt 255; $fourthOctet++) {
                    $scan = $startFirst + "." + $startSecond + "." + $thirdOctet + "." + $fourthOctet
                    Write-Output "Pinging $scan"
                    if ( Test-Connection $scan -count 1 -quiet) {
                        Write-Output "$scan is online!"
                    }
                }
            }

        }
if ($cidr -gt 0 -and $cidr -le 8)
        {

        Write-Output "cidr le 8= $cidr"
        for ($firstOctet = $startFirst; $firstOctet -lt $octet; $firstOctet++) {
            for ($secondOctet = $startScond; $secondOctet -lt $octet; $secondOctet++) {
                for ($thirdOctet = 0; $thirdOctet -lt $octet; $thirdOctet++) {
                    for ($fourthOctet = 0; $fourthOctet -lt 255; $fourthOctet++) {
                        $scan = $firstOctet + "." + $secondOctet + "." + $thirdOctet + "." + $fourthOctet
                        Write-Output "Pinging $scan"
                        if ( Test-Connection $scan -count 1 -quiet) {
                            Write-Output "$scan is online!"
                        }
                    }
                }
            }
        }

    }
}

elseif ($ipEnd) {
    $endFirst, $endSecond, $endThird, $endFourth = $ipEnd.Split(".")
    
    if ($startFirst -eq $endFirst) {
        if ($startSecond -eq $endSecond) {

            if ($startThird -eq $endThird) {

                if ($startFourth -eq $endFourth) {
                    $scan = $startFirst + "." + $startSecond + "." + $startThird + "." + $startFourth
                    Write-Output "Pinging $scan"
                    if ( Test-Connection $scan -count 1 -quiet) {
                        Write-Output "$scan is online!"
                    }
                }


            }
            else {
                for ($thirdOctet = $startThird; $thirdOctet -lt $endThird; $thirdOctet++) {
                    for ($fourthOctet = 0; $fourthOctet -lt 255; $fourthOctet++) {
                        $scan = $startFirst + "." + $startSecond + "." + $thirdOctet + "." + $fourthOctet
                        Write-Output "Pinging $scan"
                        if ( Test-Connection $scan -count 1 -quiet) {
                            Write-Output "$scan is online!"
                        }
                    }
                }
            }

        }
        else {
            for ($secondOctet = $startSecond; $secondOctet -lt $endSecond; $secondOctet++) {
                for ($thirdOctet = 0; $thirdOctet -lt 255; $thirdOctet++) {
                    for ($fourthOctet = 0; $fourthOctet -lt 255; $fourthOctet++) {
                        $scan = $startFirst + "." + $secondOctet + "." + $thirdOctet + "." + $fourthOctet
                        Write-Output "Pinging $scan"
                        if ( Test-Connection $scan -count 1 -quiet) {
                            Write-Output "$scan is online!"
                        }
                    }
                }
            }
        }

    }
    else {
        for ($firstOctet = $startFirst; $firstOctet -lt $endFirst; $firstOctet++) {
            for ($secondOctet = 0; $secondOctet -lt 255; $secondOctet++) {
                for ($thirdOctet = 0; $thirdOctet -lt 255; $thirdOctet++) {
                    for ($fourthOctet = 0; $fourthOctet -lt 255; $fourthOctet++) {
                        $scan = $firstOctet + "." + $secondOctet + "." + $thirdOctet + "." + $fourthOctet
                        Write-Output "Pinging $scan"
                        if ( Test-Connection $scan -count 1 -quiet) {
                            Write-Output "$scan is online!"
                        }
                    }
                }
            }
        }
    }
}
