### Imports ###
# Global #

# Local #
from basics import Basics
from aminos import genetic_code as aminos
### Code ###
class BioCrypter:
    def __init__(self, dna:str, *, restrictionEnzymes:list[str]=None) -> None:
        #print(restrictionEnzymes)
        DNA_str = dna
        DNA:list[str] = []
        if restrictionEnzymes != None:
            for restriction in restrictionEnzymes:
                restriction_stripped = restriction.replace("|", "")
                #print(restriction, restriction_stripped)
                DNA_str = DNA_str.replace(restriction_stripped, restriction)
            #print(DNA_str)
            for part in DNA_str.split("|"):
                DNA.append(part)
        else:
            DNA.append(DNA_str)
        self.dnaString:list[str] = DNA
        #print(self.dnaString)
        
        self.dna = []
        for dna_bunch in self.dnaString:
            codons = self.get_codons(dna_bunch)
            aminos = self.get_aminos(codons)
            pairs = [(codons[i], aminos[i]) for i in range(0, len(codons))]
            self.dna.append(pairs)
            pass

    def clean_fasta(file:str) -> str:
        with open(file, 'r') as f:
            input = f.read()
            r = ""
            for line in input.split("\n"):
                if line[0] != ">":
                    r += line
            return r

    def get_codons(self, dna:str) -> list:
        return [dna[i:i+3] for i in range(0, len(dna), 3)]

    def get_aminos(self, codons:list) -> list:
        return [aminos.get(codons[i], "Unknown") for i in range(0, len(codons))]

    def getText(self, *, addLines=False) -> str:
        ret = ""
        for dna_seg in self.dna:
            ret += "[START SEGMENT]"
            if addLines: ret += "\n"
            for bit in dna_seg:
                ret += f"{bit[0]}>{bit[1]};"
                if addLines: ret += "\n"
            ret += "[\\END SEGMENT]"
            if addLines: ret += "\n\n"
        return ret
    
### Main ###
if __name__ == "__main__":
    args = Basics.Terminal.Arguments()
    restrict = None
    if type(args.find("--restrictions")) == str:
        restrict = [args.find("--restrictions")]
    else:
        restrict = args.find("--restrictions")

    to_parse:str
    if args.find("--fasta"):
        to_parse = BioCrypter.clean_fasta(args.find("--file"))
    else:
        to_parse = Basics.File.clean_file(args.find("--file"))

    dnaObj = BioCrypter(
        to_parse,
        restrictionEnzymes=restrict
    )
    print(f"""Code length: {len(dnaObj.dnaString)}
""")
    # print(dnaObj.getText(addLines=True))
    if args.find("--output"):
        with open(args.find("--output"), 'w') as file:
            file.write(dnaObj.getText(addLines=True))
        pass