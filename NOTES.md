Test finding:
Floating point on def test_profit_calculator() was found to equal 6.4600000000001, and not 6.46 as it would in the production version. pytest.approx(6.46) was added for the test version as it cannot be represented exactly in tests.

All repeaed code was made into functions to improve the maintainability and readability of the code