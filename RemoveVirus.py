def remove_virus(drive: str) -> str:
    """Removes suspicious files (names containing "virus" or "malware") from the given drive but preserving antivirus and personal files

    Args:
        drive (str): a string containing a list of files on a pc

    Returns:
        str: the list of files after viruses and malware have been removed
    """
    good = ["anti", "not"]

    frags = drive.split()

    files = [f.strip(",") for f in frags[2:]]

    clean_files = []
    for i in files:
        if "virus" in i:
            check = i.replace("virus.exe", "")
            if check in good:
                clean_files.append(i)
        elif "malware" in i:
            check = i.replace("malware.exe", "")
            if check in good:
                clean_files.append(i)
        else:
            clean_files.append(i)
    
    if clean_files == "":
        return f"{frags[0]} {frags[1]} Empty"
    else:
        unpacked = ", ".join(clean_files)
        new_drive = f"{frags[0]} {frags[1]} {unpacked}"
        return new_drive

def main():
    """Handles test cases and pretty printing of results
    """
    test_cases = ["PC Files: spotifysetup.exe, virus.exe, dog.jpg", "PC Files: antivirus.exe, cat.pdf, lethalmalware.exe, dangerousvirus.exe ", "PC Files: notvirus.exe, funnycat.gif"]
    answers = ["PC Files: spotifysetup.exe, dog.jpg", "PC Files: antivirus.exe, cat.pdf", "PC Files: notvirus.exe, funnycat.gif"]

    for i in range(len(test_cases)):
        result = remove_virus(test_cases[i])

        assert result == answers[i]
        print(f"""remove_virus("{test_cases[i]}")
output = "{result}"\n""")

if __name__ == "__main__":
    main()