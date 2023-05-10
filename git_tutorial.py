"""
GIT - verziókezelő rendszer

Github - Microsoft
GitLab - 
Bitbucket - Atlassian

Git kezelté akarom tenni a fejlesztésem:
1. lépés: git init 
    parancs kiadása abban a mappában, amit git kezelté akarok tenni

    létrejön egy 'master' nevű branch -> a kódom 1 adott állapota


A fejlesztésem során a file-jaim / mappáimnak az következő státuszai vannak.
 - untracked - még nem git kezelt

 változás állapotai:
  - not staged állapot - a változás még nincs a stageld változásokhoz adva
  - staged állapot - ezek a változások már készen állnak a véglegesítésre, de bármikor módosítható
  - committed - ez 1 "véglegesített, időbéjeggel ellátott" állapot -> erre az adott commit állapotra
  bármikor vissza tudom állítani a fejlesztésem állapotát

a commit-ok a branch részei

HA CSAPATBAN DOLGOZOL
1. nem commitálsz közvetlenül a master / main branchra -> a master / main branch általában a kódom
éles állapotát tartalmazza

Amikor Github-ot, Gitlabot vagy ezekhez hasonló megoldást használtok,
akkor mindig lesz 2 kódbázis:

1. a remote kód - a te gépeden lévő
2. origin kód - a Github vagy Gitlabon lévő kód

Pull Request - a branchek egyesítésének a folyamata
Szoftver fejlesztésben ez a "négy szem elv"


"""