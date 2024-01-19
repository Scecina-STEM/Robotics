# Gobal Imports
import sys
# Local Imports
from aminos import genetic_code as aminos

### Main Code ###
class BioCrypter:
    # Clean a file's text
    def clean_file(file_path:str) -> str:
        file_text:str
        with open(file_path, 'r') as file:
            file_text = file.read().lower()
        file_lines:str = ""
        comment_lines:list = []
        for file_line in file_text.split("\n"):
            if file_line[0] == "#":
                comment_lines += file_line
            else:
                file_lines += file_line
        cleaned_lines:str = file_lines.strip().replace("\n", "").replace(" ", "")
        return cleaned_lines.upper()

    # Process DNA sequence
    def restriction(dna:str, restrictors:list) -> list:
        return dna.split(restrictors)

    def get_codons(dna:str) -> list:
        return [dna[i:i+3] for i in range(0, len(dna), 3)]

    def get_aminos(codons:list) -> list:
        return [aminos.get(codons[i], "Unknown") for i in range(0, len(codons))]
    
    def process_dna(dna:str) -> tuple:
        codons:list = BioCrypter.get_codons(file_cont)
        aminos:list = BioCrypter.get_aminos(codons)
        return (codons, aminos)


### Start Code ###
if __name__ == "__main__":
    print(sys.argv)
    file_path:str
    if sys.argv.__len__() == 1:
        file_path = input("FilePath > ")
    else:
        file_path = sys.argv[1]
    print(f"FilePath: {file_path}")
    file_cont = BioCrypter.clean_file(file_path)
    res:tuple = BioCrypter.process_dna(file_cont)
    special:dict = {
        "AddLines": False
    }
    try:
        if sys.argv.index("--AddLines") != ValueError:
            special["AddLines"] = True
    except:
        pass
    try:
        if sys.argv.index("--output") != ValueError:
            output_file_arg_index = sys.argv.index("--output") + 1
            output_fp = sys.argv[output_file_arg_index]
            to_out:str = ""
            for index in range(0, len(res[0])):
                codon = res[0][index]; amino = res[1][index]
                to_out += f"{codon}>{amino};"

            with open(output_fp, 'w') as output:
                if special["AddLines"]:
                    output.write(to_out.replace(";", ";\n"))
                else:
                    output.write(to_out)
    except:
        pass

                