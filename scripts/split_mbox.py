import mailbox, os

# 1. point at your mbox file
mbox_path = "data/nazario/phishing-2023"
out_dir  = "data/nazario/txt"
os.makedirs(out_dir, exist_ok=True)

# 2. open and iterate
mbox = mailbox.mbox(mbox_path)
for i, message in enumerate(mbox):
    # get the raw body (decode any base64/quoted-printable)
    payload = message.get_payload(decode=True) or b""
    text    = payload.decode(errors="ignore")

    # 3. write one file per message
    fname = os.path.join(out_dir, f"phish_{i:05d}.txt")
    with open(fname, "w", encoding="utf-8") as f:
        f.write(text)
