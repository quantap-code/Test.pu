name: Build EXE
on: push
jobs:
  build:
    runs-on: windows-latest
    steps:
    - uses: actions/checkout@v4
    - uses: actions/setup-python@v5
      with:
        python-version: '3.10'
    - run: pip install pyinstaller
    - run: pyinstaller --onefile --noconsole --name Test Test.py
    - uses: actions/upload-artifact@v4
      with:
        name: Test-exe
        path: dist/Test.exe
