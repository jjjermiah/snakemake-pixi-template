rule all:
    input:
        "results/summary.txt",
    shell:
        "cat {input}"

rule makesummary:
    output:
        "results/summary.txt",
    container:
      "docker://bhklab/annotationgx-r:0.0.0.9095"
    shell:
        "sleep 10; echo 'This is a summary' > {output}"
