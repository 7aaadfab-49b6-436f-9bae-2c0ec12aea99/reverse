#define _GNU_SOURCE
#include <stdio.h>
#include <stdarg.h>
#include <string.h>
#include <dlfcn.h>
#include <sys/ptrace.h>
#include <fcntl.h>

long ptrace(enum __ptrace_request request, ...) {
    /* Always report success: no tracer, no error */
    return 0;
}

static int (*real_open)(const char *, int, ...) = NULL;

int open(const char *pathname, int flags, ...) {
    if (!real_open) real_open = dlsym(RTLD_NEXT, "open");
    if (pathname && strcmp(pathname, "/proc/self/status") == 0) {
        return real_open("/tmp/fake_status_no_tracer", flags);
    }
    va_list ap;
    va_start(ap, flags);
    mode_t mode = va_arg(ap, mode_t);
    va_end(ap);
    return real_open(pathname, flags, mode);
}
