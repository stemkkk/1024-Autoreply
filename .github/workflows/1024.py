name: 1024-AutoReply

on:
  workflow_dispatch: # 手动触发
  push:
    branches:
      - Multi_User
  schedule:
    - cron: '15 9,21 * * *'


jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: checkout actions
      run : |
        sudo apt-get update
        sudo apt-get -y install git
        sudo apt-get -y install python3-pip
        sudo apt-get -y install python3-setuptools

    - name: install env
      run :

        pip3 install requests onetimepass pillow

    - name: run cl.298y.xyz
      env:
        USER: ${{ secrets.USER }}
        PASSWORD: ${{ secrets.PASSWORD }}
        SECRET: ${{ secrets.SECRET }}
        TOKER: ${{ secrets.TOKER }}
        CODEUSER: ${{ secrets.CODEUSER }}
        CODEPASS: ${{ secrets.CODEPASS }}
      run:
        python3 cl.298y.xyz
