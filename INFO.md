# Mark
Mark are marking, tags, we put on our test to define important points.
It creates test groups.
For example, if we want to run all the tests which return "goiabada", we could mark those tests with `@mark.goiabada` for example.
To use it, we need to use `from pytest import mark`.
We could also run:

```
@mark.database
def test_anything():
    pass
    
pytest -m "not database"
```
Important functions and special marks:
 - @mark.skip - jump a test
 - @mark.skipif - jump a test in some context
 - @mark.usefixture - To use a fixture
 - @mark.parametrize - Parametrizing a test


# Fixtures
Fixtures are a way to "join in a context", or provide some data or tool that must be executed out the test suit.