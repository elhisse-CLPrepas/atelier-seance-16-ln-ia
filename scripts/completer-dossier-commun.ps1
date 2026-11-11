param([string]$Destination = (Join-Path $PSScriptRoot '../../atelier-seance-15-ln-ia/mon-dossier-challenge-module04'))
$ErrorActionPreference = 'Stop'
$sourceRoot = Split-Path $PSScriptRoot -Parent
$destinationRoot = [IO.Path]::GetFullPath($Destination)
$copies = @(
    @{ Source = 'OUVRIR-SEANCE-16.html'; Target = 'OUVRIR-SEANCE-16.html' },
    @{ Source = 'public/ressources'; Target = '06-ressources/seance-16/ressources' },
    @{ Source = 'kit-candidat/05-automatisation'; Target = '05-automatisation' },
    @{ Source = 'kit-candidat/sources-fictives'; Target = '06-ressources/seance-16/sources-fictives' },
    @{ Source = 'kit-candidat/07-portfolio/entree-preuve-16.md'; Target = '07-portfolio/entree-preuve-16.md' },
    @{ Source = 'kit-candidat/07-portfolio/relais-module-05.md'; Target = '07-portfolio/relais-module-05.md' },
    @{ Source = 'public/ressources/atelier/poursuivre-s16.md'; Target = '00-pilotage/POURSUIVRE-S16.md' }
)
$journal = @()
foreach ($copy in $copies) {
    $source = Join-Path $sourceRoot $copy.Source
    $items = if (Test-Path -LiteralPath $source -PathType Container) { Get-ChildItem -LiteralPath $source -File -Recurse } else { Get-Item -LiteralPath $source }
    foreach ($item in $items) {
        $relative = if (Test-Path -LiteralPath $source -PathType Container) { Join-Path $copy.Target $item.FullName.Substring($source.Length + 1) } else { $copy.Target }
        $target = [IO.Path]::GetFullPath((Join-Path $destinationRoot $relative))
        if (-not $target.StartsWith($destinationRoot + [IO.Path]::DirectorySeparatorChar, [StringComparison]::OrdinalIgnoreCase)) { throw 'Destination hors du dossier commun.' }
        if (Test-Path -LiteralPath $target) {
            $journal += "CONSERVE $relative"
        } else {
            New-Item -ItemType Directory -Path (Split-Path $target -Parent) -Force | Out-Null
            Copy-Item -LiteralPath $item.FullName -Destination $target
            $journal += "AJOUTE $relative"
        }
    }
}
$journal
