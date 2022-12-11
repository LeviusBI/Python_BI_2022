# Python_BI_2022
Тут я буду ~~говнокодить~~ **решать ДЗ**

In this HW I will performance scripts, that will be able to work from command line. I will use os and sys modules to do my best. I am obliged to do 4 functions and also have 4 optional functions.  

Requirements:

1. Each program is in a separate script, which is named after the template `utility_name`.py. That is, the analogue of wc will be called wc.py, grep - grep.py, etc.
2. Each of the programs must use the python interpreter from the current active environment (we did not go through this, but it is easy to google) and have execution rights
3. Utilities must be able to pipeline with each other and with UNIX utilities. For example, ./ls.py | ./grep.py fastq | ./wc.py -l or cat *.tsv | sort | ./uniq.py | ./wc.py -l. But if the ability to work in pipelines is not provided initially (for example, cp, mv, etc.), then it is not necessary to implement it.
4. Like the reference utilities, ours should be able to accept an argument or a stream as input. For example, ls needs to be passed an argument (ls some_dir, where some_dir is an argument, the default is the current directory), sort can be passed a filename (sort annotation.gff) or a stream (cat annotation.gff | sort).
5. Create a repository (description of program features, installation, launch, usage examples)
The use of downloadable third-party modules is prohibited. Only the standard library can be used (except for the subprocess module).
6. Running scripts should be possible without the python command (i.e. ./wc.py file.txt instead of python wc.py file.txt)

Programs required for implementation (7 points for each):

1. wc with options -l -w -c
2. ls with -a option
3. sort without options
4. rm with -r option
