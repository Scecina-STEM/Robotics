from team.basics import Basics

argu = Basics.Terminal.Arguments()

argu.find("--s")
argu.findRun("--d", lambda val: print(f"ff {val}"))