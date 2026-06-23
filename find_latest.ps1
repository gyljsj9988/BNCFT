[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$file = Get-ChildItem -Path "f:\BNCFT" -Recurse -File | Sort-Object LastWriteTime -Descending | Select-Object -First 1
Write-Output "文件路径: $($file.FullName)"
Write-Output "最后修改时间: $($file.LastWriteTime)"
