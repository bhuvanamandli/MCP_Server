from fastmcp import FastMCP

mcp = FastMCP('Financial Report Summarizer')


@mcp.tool
def get_financial_report():
    """
    Retrieves financial reports for each year.
    """
    return {
        2022: {
            "revenue": "₹30 Crores",
            "expenses": "₹40 Crores",
            "net_loss": "₹10 Crores",
            "growth": "-5%",
            "status": "Loss"
        },
        2023: {
            "revenue": "₹40 Crores",
            "expenses": "₹50 Crores",
            "net_loss": "₹10 Crores",
            "growth": "-3%",
            "status": "Loss"
        },
        2024: {
            "revenue": "₹80 Crores",
            "expenses": "₹55 Crores",
            "net_profit": "₹25 Crores",
            "growth": "15%",
            "status": "Profitable"
        },
        2025: {
            "revenue": "₹100 Crores",
            "expenses": "₹68 Crores",
            "net_profit": "₹32 Crores",
            "growth": "18%",
            "status": "Profitable"
        },
        2026: {
            "revenue": "₹125 Crores",
            "expenses": "₹82 Crores",
            "net_profit": "₹43 Crores",
            "growth": "20%",
            "status": "Profitable"
        }
    }


@mcp.tool
def get_revenue_comparison():
    """
    Returns the highest and lowest revenue years.
    """
    return {
        "Highest revenue year": "2026",
        "Highest revenue": "₹125 Crores",
        "Lowest revenue year": "2022",
        "Lowest revenue": "₹30 Crores"
    }


@mcp.tool
def total_profit_and_loss():
    """
    Returns the overall profit and loss summary.
    """
    return {
        "total_profit": "₹100 Crores",
        "total_loss": "₹20 Crores",
        "profit": "yes",
        "loss": "yes",
        "status": "Overall profitable"
    }


if __name__ == "__main__":
    mcp.run()
