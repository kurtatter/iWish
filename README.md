# iWish

Для того чтобы запустить программу, сначала необходимо перейти в директорию проекта и создать виртуальное окружение

Если у вас Linux:

```bash
python3 -m venv venv
```

Если у вас Windows:

```bash
python -m venv venv
```

После следует активировать виртуальное окружение

Linux

```bash
source venv/bin/activate
```

Windows

```bash
 cmd.exe /k "%CD%\venv\Scripts\activate"
```

После, следует установить необходимые пакеты

```bash
pip install -r requests.txt
```

После, следует запустить скрипт

Linux

```bash
python3 iwish.py
```

Windows:

```bash
python iwish.py
```