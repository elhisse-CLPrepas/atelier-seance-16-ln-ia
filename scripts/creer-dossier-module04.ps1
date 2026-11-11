param([string]$Source = (Join-Path $PSScriptRoot '../../atelier-seance-15-ln-ia/mon-dossier-challenge-module04'))
$ErrorActionPreference = 'Stop'
$atelier = Split-Path $PSScriptRoot -Parent
$destination = Join-Path $atelier 'mon-dossier-challenge-MODULE-04'
function Copier-SansRemplacer([string]$Origine, [string]$Cible) {
    New-Item -ItemType Directory -Path $Cible -Force | Out-Null
    foreach ($element in Get-ChildItem -LiteralPath $Origine -Force) {
        if ($element.Name -in @('.git', 'node_modules', '.venv', '__pycache__', '02-PROMPT')) { continue }
        $chemin = Join-Path $Cible $element.Name
        if ($element.PSIsContainer) { Copier-SansRemplacer $element.FullName $chemin }
        elseif (-not (Test-Path -LiteralPath $chemin)) { Copy-Item -LiteralPath $element.FullName -Destination $chemin }
    }
}
if (-not (Test-Path -LiteralPath $Source -PathType Container)) { throw 'Dossier de progression S15 introuvable.' }
Copier-SansRemplacer $Source $destination
Copier-SansRemplacer (Join-Path $atelier 'public/ressources/demo') (Join-Path $destination '08-demonstration/guide/ressources')
Copier-SansRemplacer (Join-Path $atelier 'public/ressources/sources') (Join-Path $destination '08-demonstration/guide/sources')
Copier-SansRemplacer (Join-Path $atelier 'kit-candidat/sources-fictives/samira') (Join-Path $destination '08-demonstration/samira')
Copier-SansRemplacer (Join-Path $atelier 'public/ressources/affiches') (Join-Path $destination '06-ressources/affiches')
$nouvelAtelier = Join-Path $destination 'OUVRIR-SEANCE-16.html'
if (-not (Test-Path -LiteralPath $nouvelAtelier)) { Copy-Item -LiteralPath (Join-Path $atelier 'OUVRIR-SEANCE-16.html') -Destination $nouvelAtelier }
Write-Output "Dossier de progression disponible : $destination"
Write-Output 'Les fichiers existants ont ete conserves. Aucun historique Git copie.'
