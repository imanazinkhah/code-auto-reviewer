from reviewer.syntax_checker import check_syntax
from reviewer.quality_checker import check_quality
from reviewer.function_analyzer import analyze_functions
from reviewer.complexity_analyzer import analyze_complexity
from reviewer.security_checker import check_security
from reviewer.report import generate_report
from reviewer.html_report import generate_html_report


def main():

    print("================================")
    print("      Code Auto Reviewer")
    print("================================")

    file_path = input("Enter Python file path: ")

    # Syntax Check

    syntax_result = check_syntax(file_path)

    if not syntax_result["valid"]:

        error = syntax_result["error"]

        print("\n❌ Syntax Error")
        print(f"Line: {error['line']}")
        print(f"Column: {error['column']}")
        print(f"Message: {error['message']}")

        return

    # Quality Check

    quality_issues = check_quality(file_path)

    # Function Analysis

    function_results = analyze_functions(file_path)

    # Complexity Analysis

    complexity_results = analyze_complexity(file_path)

    # Security Analysis

    security_issues = check_security(file_path)

    # Generate Final Report

    generate_report(
        file_path,
        syntax_result,
        quality_issues,
        function_results,
        complexity_results,
        security_issues
    )


    score = generate_report(
    file_path,
    syntax_result,
    quality_issues,
    function_results,
    complexity_results,
    security_issues
)

    generate_html_report(
    file_path,
    syntax_result,
    quality_issues,
    function_results,
    complexity_results,
    security_issues,
    score
)


if __name__ == "__main__":
    main()