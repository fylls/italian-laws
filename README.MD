<div align="center">

# Italian Laws: The ultimate spaghetti code

If you are a **human**, you can find them all [here](https://www.normattiva.it/staticPage/codici)

If you are a **computer**, please read `index.tsv`

<br>

![image](https://user-images.githubusercontent.com/55017307/216944897-2ec94c88-3051-40fe-a0ce-2af89caf9bb3.png)

**image 1:** epitome of italian driven design

</div>

----

## Environment Setup

**easy way**

```bash
$ pip install -r requirements.txt
```

<br />

**long (italian) way**

```bash
$ conda create -n spaghetti
```

```bash
$ conda activate spaghetti
```

```bash
$ pip install pdfminer.six
```

```bash
$ pip freeze > requirements.txt
```

<br />

**you can now run the following commands**

```bash
$ python3 spaghetti-scraper.py
$ python3 spaghetti-parser.py
$ python3 spaghetti-combiner.py
```

---

