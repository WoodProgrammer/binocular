curl -LO https://github.com/ericchiang/containers-from-scratch/releases/download/v0.1.0/rootfs.tar.gz
tar -zxf rootfs.tar.gz
PID_OF_TARGET=$(pidof coredns|awk '{print $1}')
mount -t proc proc $PWD/rootfs/proc
nsenter --pid=/proc/$PID_OF_TARGET/ns/pid unshare -f --mount-proc=$PWD/rootfs/proc chroot rootfs /bin/bash