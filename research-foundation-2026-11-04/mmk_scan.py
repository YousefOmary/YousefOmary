# mmk_scan.py
# Mechanical first pass over the Sanskrit MMK (GRETIL text, 448 verses) for
# the test in file 18. It does NOT classify; it extracts the verses that carry
# each of the three idioms the text uses, so that the manual classification
# starts from a list produced by rule rather than by choice.
#   refutation idiom : na yujyate / nopapadyate / katham / kutah / prasajyate / na vidyate / nasti
#   withholding idiom: nivrtta / upasama / prajnapti / vaktavya / desita / drsti / prapanca / ajyate
# Usage: python3 -I mmk_scan.py path/to/mmk_sanskrit.txt
import re, sys, json

path = sys.argv[1]
t = open(path, encoding="utf-8").read()
verses = re.findall(r"(.*?)//\s*MMK_(\d+)\.(\d+)\s*//", t, flags=re.S)

REF = r"yujyate|upapadyate|upapatsyate|katham|kutaḥ|kasmāt|prasajyate|prasakt|na vidyate|nāsti|naiva|nopa"
WITH = r"nivṛtt|upaśam|prajñapt|prajñapy|vaktavy|deśit|deśay|dṛṣṭi|prapañc|ajyate|nirvikalp|kathyate|ucyate|udāhṛt"

rows = []
for body, ch, v in verses:
    b = " ".join(body.split())
    rows.append({
        "verse": f"{ch}.{v}",
        "refutation_idiom": bool(re.search(REF, b)),
        "withholding_idiom": bool(re.search(WITH, b)),
        "text": b,
    })

n = len(rows)
ref = [r for r in rows if r["refutation_idiom"]]
wit = [r for r in rows if r["withholding_idiom"]]
neither = [r for r in rows if not r["refutation_idiom"] and not r["withholding_idiom"]]
out = {
    "verses": n,
    "with refutation idiom": len(ref),
    "with withholding idiom": len(wit),
    "with neither (plain assertion candidates)": len(neither),
    "withholding-idiom verses": [r["verse"] for r in wit],
    "plain candidates": [r["verse"] for r in neither],
}
print(json.dumps(out, ensure_ascii=False, indent=1))
