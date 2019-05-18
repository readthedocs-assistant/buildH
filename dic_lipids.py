# dic for reconstructing hydrogens in POPC
# Format:
# dic= { "atom1": ("typeofH2build", "helper1", "helper2"),
#        "atom2": ("typeofH2build", "helper1", "helper2"),
#        ...}
        # choline
POPC = {"C5": ("CH2", "N4", "C6"),
        "C6": ("CH2", "C5", "O7"),
        # glycerol
        "C12": ("CH2", "O11", "C13"),
        "C13": ("CH", "C12", "C32", "O14"),
        "C32": ("CH2", "C13", "O33"),
        # sn2
        "C17": ("CH2", "C15", "C18"),
        "C18": ("CH2", "C17", "C19"),
        "C19": ("CH2", "C18", "C20"),
        "C20": ("CH2", "C19", "C21"),
        "C21": ("CH2", "C20", "C22"),
        "C22": ("CH2", "C21", "C23"),
        "C23": ("CH2", "C22", "C24"),
         # C24=C25 --> double bond
        "C24": ("CHdoublebond", "C23", "C25"),
        "C25": ("CHdoublebond", "C24", "C26"),
        "C26": ("CH2", "C25", "C27"),
        "C27": ("CH2", "C26", "C28"),
        "C28": ("CH2", "C27", "C29"),
        "C29": ("CH2", "C28", "C30"),
        "C30": ("CH2", "C29", "C31"),
        "C31": ("CH2", "C30", "CA1"),
        "CA1": ("CH2", "C31", "CA2"),
        # sn1
        "C36": ("CH2", "C34", "C37"),
        "C37": ("CH2", "C36", "C38"),
        "C38": ("CH2", "C37", "C39"),
        "C39": ("CH2", "C38", "C40"),
        "C40": ("CH2", "C39", "C41"),
        "C41": ("CH2", "C40", "C42"),
        "C42": ("CH2", "C41", "C43"),
        "C43": ("CH2", "C42", "C44"),
        "C44": ("CH2", "C43", "C45"),
        "C45": ("CH2", "C44", "C46"),
        "C46": ("CH2", "C45", "C47"),
        "C47": ("CH2", "C46", "C48"),
        "C48": ("CH2", "C47", "C49"),
        "C49": ("CH2", "C48", "C50")}

