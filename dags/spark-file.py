from pyspark.sql import SparkSession
from pyspark.sql import Row

def main():
    # Initialize Spark Session
    spark = SparkSession.builder \
        .appName("Test Spark DataFrame") \
        .getOrCreate()

    # Sample data
    data = [Row(name="Alice", age=25),
            Row(name="Bob", age=30),
            Row(name="Charlie", age=35)]

    # Create DataFrame
    sample_df = spark.createDataFrame(data)

    # Show the DataFrame
    sample_df.show()

    # Stop the Spark Session
    spark.stop()

if __name__ == "__main__":
    main()
