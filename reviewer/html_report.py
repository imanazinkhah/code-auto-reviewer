def generate_html_report(
    file_path,
    syntax_result,
    quality_issues,
    function_results,
    complexity_results,
    security_issues,
    score
):

    html = f"""
<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="UTF-8">

    <title>Code Auto Reviewer</title>

    <style>

        body {{
            font-family: Arial, sans-serif;
            background: #f4f6f8;
            margin: 0;
            padding: 40px;
        }}

        .container {{
            max-width: 900px;
            margin: auto;
            background: white;
            padding: 30px;
            border-radius: 12px;
        }}

        h1 {{
            margin-bottom: 5px;
        }}

        .file {{
            color: #666;
            margin-bottom: 30px;
        }}

        .score {{
            font-size: 48px;
            font-weight: bold;
            margin: 20px 0;
        }}

        .section {{
            margin-top: 30px;
        }}

        .item {{
            padding: 15px;
            margin: 10px 0;
            border-radius: 8px;
            background: #f1f3f5;
        }}

        .success {{
            color: green;
        }}

        .warning {{
            color: orange;
        }}

        .danger {{
            color: red;
        }}

    </style>

</head>

<body>

<div class="container">

    <h1>🔍 Code Auto Reviewer</h1>

    <div class="file">
        File: {file_path}
    </div>

    <div class="score">
        ⭐ {score}/100
    </div>

    <div class="section">

        <h2>📋 Review Summary</h2>

        <div class="item">
            Syntax:
            {"<span class='success'>✅ PASS</span>"
            if syntax_result["valid"]
            else "<span class='danger'>❌ FAIL</span>"}
        </div>

        <div class="item">
            Quality:
            {len(quality_issues)} issues
        </div>

        <div class="item">
            Functions:
            {len(function_results)} found
        </div>

        <div class="item">
            Security:
            {len(security_issues)} issues
        </div>

    </div>

    <div class="section">

        <h2>⚠️ Quality Issues</h2>

"""

    if quality_issues:

        for issue in quality_issues:

            html += f"""
        <div class="item warning">

            Line {issue["line"]}:
            {issue["message"]}

        </div>
"""

    else:

        html += """
        <div class="item success">
            ✅ No quality issues found.
        </div>
"""

    html += """

    </div>

    <div class="section">

        <h2>🔐 Security Issues</h2>

"""

    if security_issues:

        for issue in security_issues:

            html += f"""
        <div class="item danger">

            Line {issue["line"]}

            <br>

            Severity: {issue["severity"]}

            <br>

            {issue["message"]}

        </div>
"""

    else:

        html += """
        <div class="item success">
            ✅ No obvious security issues found.
        </div>
"""

    html += """

    </div>

    <div class="section">

        <h2>🔧 Functions</h2>

"""

    if function_results:

        for function in function_results:

            html += f"""
        <div class="item">

            <strong>{function["name"]}</strong>

            <br>

            Line: {function["line"]}

            <br>

            Parameters: {function["parameters"]}

            <br>

            Lines: {function["lines"]}

        </div>
"""

    else:

        html += """
        <div class="item">
            No functions found.
        </div>
"""

    html += """

    </div>

</div>

</body>

</html>
"""

    with open("report.html", "w", encoding="utf-8") as file:

        file.write(html)

    print("\n📄 HTML report created: report.html")