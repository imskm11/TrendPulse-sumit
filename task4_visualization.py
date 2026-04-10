import pandas as pd
import matplotlib.pyplot as plt
import os

# Input file
INPUT_FILE = "data/trends_cleaned.csv"


def main():
    # Check file
    if not os.path.exists(INPUT_FILE):
        print(f"File not found: {INPUT_FILE}")
        return

    # Load data
    try:
        df = pd.read_csv(INPUT_FILE)
    except Exception as e:
        print(f"Error loading file: {e}")
        return

    print("Generating visualizations...")

    
    # 1. Posts per category
    
    category_counts = df["category"].value_counts()

    plt.figure()
    category_counts.plot(kind="bar")
    plt.title("Posts per Category")
    plt.xlabel("Category")
    plt.ylabel("Number of Posts")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("data/posts_per_category.png")
    plt.show()

    
    # 2. Average score per category
    
    avg_score = df.groupby("category")["score"].mean()

    plt.figure()
    avg_score.plot(kind="bar")
    plt.title("Average Score per Category")
    plt.xlabel("Category")
    plt.ylabel("Average Score")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("data/avg_score.png")
    plt.show()

    
    # 3. Average comments per category
    
    avg_comments = df.groupby("category")["num_comments"].mean()

    plt.figure()
    avg_comments.plot(kind="bar")
    plt.title("Average Comments per Category")
    plt.xlabel("Category")
    plt.ylabel("Average Comments")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("data/avg_comments.png")
    plt.show()

    
    # 4. Score distribution
    
    plt.figure()
    plt.hist(df["score"], bins=20)
    plt.title("Score Distribution")
    plt.xlabel("Score")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig("data/score_distribution.png")
    plt.show()

    
    # 5. Category share (pie chart)
    
    plt.figure()
    category_counts.plot(kind="pie", autopct="%1.1f%%")
    plt.title("Category Share")
    plt.ylabel("")  # remove default ylabel
    plt.tight_layout()
    plt.savefig("data/category_share.png")
    plt.show()

    print("All graphs generated and saved in data/ folder.")


if __name__ == "__main__":
    main()