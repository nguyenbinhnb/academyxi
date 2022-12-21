pytest -v -m "smoke" --html=Reports\\report.html testCases
rem pytest -v -m "smoke or regression" --html=Reports\\report.html testCases
rem pytest -v -m "regression" --html=Reports\\report.html testCases
rem pytest -v -m "sanity" --html=Reports\\report.html testCases
rem pytest -v -k "validate_prices_on" --html=Reports\\report.html testCases
















                                                                                    pause