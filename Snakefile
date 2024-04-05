rule all:
    input:
        "results/summary.txt",
    shell:
        "cat {input}"


rule makesummary:
    output:
        "results/summary.txt",
    shell:
        "sleep 10; echo 'This is a summary' > {output}"
