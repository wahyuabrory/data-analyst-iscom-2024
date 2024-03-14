# Introduction to Data Analysis

Data analysis is a process of inspecting, cleansing, transforming, and modeling data with the goal of discovering useful information, informing conclusions, and supporting decision-making. Data analysis has multiple facets and approaches, encompassing diverse techniques under a variety of names, and is used in different business, science, and social science domains. In today's world, data is the new oil. It is the most valuable resource in the world.

## 🕹️ Table of Contents

- [🌀 Data Analytics Life Cycle](#-data-analytics-life-cycle)
- [👨🏻‍💼 Career Roles in The Data Analytics Lifecycle](#-career-roles-in-the-data-analytics-lifecycle)
- [🔬 Analyst vs. Scientist vs. Engineer](#-analyst-vs-scientist-vs-engineer)

## 🌀 Data Analytics Life Cycle

```mermaid
graph TD
   subgraph Ask
       A1[Define the problem,<br>questions, and requirements]
   end

   subgraph Prepare
       B1[Collect data from<br>various sources]
       B2[Integrate data sources]
       B3[Clean and preprocess data]
   end

   subgraph Process
       C1[Transform data]
       C2[Model data]
   end

   subgraph Analyze
       D1[Explore data]
       D2[Visualize data]
       D3[Discover insights]
   end

   subgraph Share
       E1[Communicate findings]
       E2[Present recommendations]
   end

   subgraph Act
       F1[Implement changes]
       F2[Monitor impact]
  end
   A1 --> B1
   B1 --> B2
   B2 --> B3
   B3 --> C1
   C1 --> C2
   C2 --> D1
   D1 --> D2
   D2 --> D3
   D3 --> E1
   E1 --> E2
   E2 --> F1
   F1 --> F2
   F2 --> A1
```

## 👨🏻‍💼 Career Roles in The Data Analytics Lifecycle

```mermaid
graph TD
    subgraph Business Understanding
        A[Analyze the Business Problem]:::analyzeProb --- B[("Business Analyst<br>Understand business objectives<br>and frame the problem")]
    end

    subgraph Data Acquisition
        B --> C[("Data Engineer<br>Source, ingest, and store data<br>from various sources")]
    end

    subgraph Data Preparation
        C --> D[("Data Engineer<br>Prepare, clean, and normalize data<br>for analysis")]
    end

    subgraph Data Analysis
        D --> E[("Data Analyst<br>Explore data, perform statistical analysis,<br>and uncover insights")]
    end

    subgraph Modeling
        E --> F[("Data Scientist<br>Build and evaluate predictive models<br>using machine learning")]
    end

    subgraph Deployment
        F --> G[("Machine Learning Engineer<br>Deploy and integrate predictive models<br>into production systems")]
    end

    subgraph Business Implementation
        G --> H[("Data Engineer, Application Developer<br>Utilize deployed models to drive<br>business processes and decision-making")]
    end
```

## 🔬 Analyst vs. Scientist vs. Engineer

| Data Engineer                                                                                    | Data Analyst                                                                              | Data Scientist                                                                               |
| ------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| ![](../assets/data-engineering-icon.png)                                                         | ![data analyst icon](../assets/data-analyst-icon.png)                                     | ![](../assets/data-scientist-icon.png)                                                       |
| Build and optimize the systems that allow data scientist and data analysis to perform their work | Deliver value by analyzing dat, communicating the results to help make business decisions | Use data to solve business problems                                                          |
| **Requirement:** <br>1. Strong Programming Skills <br> 2. Cloung Computing tech <br> 3. Big Data | **Requirement:** <br> 1. Communication Skills <br> 2. Business savvy/ Domain Knowledge    | **Requirement:** <br> 1. Statistics <br> 2. Math <br> 3. Programming Skills <br> 4. Big Data |

##
