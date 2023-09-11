#include<dlfcn.h>
#include<iostream>

#include<static/static.h>
#include<shared/shared.h>

void print_module() {
    void *handle;
    void (*func)();
    handle = dlopen("./build/src/lib/module/libMyApp_Module.so", RTLD_LAZY);
    if (!handle) {
        std::fprintf(stderr, "%s\n", dlerror());
        exit(1);
    }
    dlerror();
    func = (void(*)())dlsym(handle, "print_module");
    if (!func) {
        fprintf(stderr, "Error loading symbol: %s\n", dlerror());
        dlclose(handle);
        return;
    }
    func();
    dlclose(handle);
}

int main() {
    print_static();
    print_shared();
    print_module();
    return 0;
}