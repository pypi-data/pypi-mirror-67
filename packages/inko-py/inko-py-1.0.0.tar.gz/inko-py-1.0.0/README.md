<h1 align="center">
    <img height="250" src="https://github.com/738/inko/blob/master/images/inko_logo.png?raw=true" />
    <br> Inko.py
</h1>

<p align="center">
  <b>Open Source Library, Converting Misspelled English characters into Korean letters (& vice versa)</b></br>
  <b>Python implementation of <a href="https://github.com/738/inko">Inko.js</a></b></br>
</p>

<br />

# Getting Started

## Requirements

- Python >= 3.6

## Installation

```bash
python -m pip install inko-py
```

## Usage

```python
import inko
myInko = inko.Inko()
```

or

```python
from inko import Inko
myInko = Inko()
```

### 영어(en) -> 한글(ko)

```python
print(myInko.ko2en('ㅗ디ㅣㅐ 재깅!'))
# output: hello world!
```

### 한글(ko) -> 영어(en)

```python
print(myInko.en2ko('dkssudgktpdy tptkd!'))
# output: 안녕하세요 세상!
```

### Optional parameter

| Key                  | Type    | Value         | Description     |
| -------------------- | ------- | ------------- | --------------- |
| allowDoubleConsonant | Boolean | True or False | 복자음 설정여부 |

#### 설정을 부여하는 방법은 아래의 세 가지 방법으로 지원합니다.

1. 인스턴스 생성할 때 생성자의 인자로 설정 부여

```python
from inko import Inko
myInko = Inko(allowDoubleConsonant=True)
```

2. `config` 함수로 설정 부여

```python
myInko.config(allowDoubleConsonant=True)
```

3. `en2ko` 함수의 인자로 설정 부여

```python
myInko.en2ko('rtrt', allowDoubleConsonant=True);
# output: ㄳㄳ
myInko.en2ko('rtrt', {allowDoubleConsonant=False);
# output: ㄱㅅㄱㅅ
```

## Related

- [inko-js](https://github.com/738/inko) - Inko javascript library
- [inko-cli](https://github.com/738/inko-cli) - Use inko on the command line
- [inko-web](https://github.com/738/inko-web) - Inko official website
- [inko-chrome-extension](https://github.com/738/inko-chrome-extension) - Inko chrome extension
- [alfred-inko](https://github.com/738/alfred-inko) - Alfred 3 workflow to convert misspelled English characters into Korean letters (& vice versa)

## Contributing

이 오픈소스 프로젝트에 누구나 기여할 수 있습니다. 기여하고 싶은 분들은 이 레포지토리를 포크한 후 풀리퀘스트 요청해주세요!

## License

Inko.py is released under the MIT License. See [LICENSE](https://github.com/JackCme/inko.py/blob/master/LICENSE) file for details.

## Credits

Thanks to [Jon Jee(738)](https://github.com/738), the original author of Inko.js
