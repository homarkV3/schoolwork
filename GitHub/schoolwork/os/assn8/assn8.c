#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <dirent.h>
#include <string.h>
#include <stdlib.h>

void do_ls(char [], int *);
void list_dir(char *, int *);

int main(int ac, char *av[]) {
    int total_size = 0;

    if (ac == 1) {
        do_ls(".", &total_size);
    } else {
        while (--ac) {
            printf("%s:\n", *++av);
            do_ls(*av, &total_size);
        }
    }
    
    printf("\nTotal file space used: %d\n", total_size);
    return 0;
}

void do_ls(char dirname[], int *total_size) {
    DIR *dir_ptr;
    struct dirent *direntp;
    struct stat info;

    if ((dir_ptr = opendir(dirname)) == NULL) {
        fprintf(stderr, "ls01: cannot open %s\n", dirname);
    } else {
        while ((direntp = readdir(dir_ptr)) != NULL) {
            char *path;
            asprintf(&path, "%s/%s", dirname, direntp->d_name);
            lstat(path, &info);

            if (S_ISDIR(info.st_mode)) {
                if (strcmp(direntp->d_name, ".") != 0 && strcmp(direntp->d_name, "..") != 0) {
                    printf("dir %s\n", path);
                    do_ls(path, total_size);
                }
            } else if (S_ISREG(info.st_mode)) {
                printf("  %d:%s\n", (int)info.st_size, direntp->d_name);
                *total_size += info.st_size;
            }

            free(path);
        }
        closedir(dir_ptr);
    }
}