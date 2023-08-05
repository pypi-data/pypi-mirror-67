
/*---------------------------------------------------------------*/
/*--- begin                               libvex_basictypes.h ---*/
/*---------------------------------------------------------------*/

/*
   This file is part of Valgrind, a dynamic binary instrumentation
   framework.

   Copyright (C) 2004-2015 OpenWorks LLP
      info@open-works.net

   This program is free software; you can redistribute it and/or
   modify it under the terms of the GNU General Public License as
   published by the Free Software Foundation; either version 2 of the
   License, or (at your option) any later version.

   This program is distributed in the hope that it will be useful, but
   WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
   General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program; if not, write to the Free Software
   Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
   02110-1301, USA.

   The GNU General Public License is contained in the file COPYING.

   Neither the names of the U.S. Department of Energy nor the
   University of California nor the names of its contributors may be
   used to endorse or promote products derived from this software
   without prior written permission.
*/

#ifndef __LIBVEX_BASICTYPES_H
#define __LIBVEX_BASICTYPES_H

/* This is where we bootstrap msvc compatibility */
#ifndef _MSC_VER /* gcc/clang/etc stuff */
#define LIKELY(x)       __builtin_expect(!!(x), 1)
#define UNLIKELY(x)     __builtin_expect(!!(x), 0)
#define CAST_AS(x)      (__typeof__(x))

#else /* msvc stuff */
#define LIKELY(x)       (x)
#define UNLIKELY(x)     (x)
#define CAST_AS(x)

#define __builtin_memset memset
#define __builtin_memcpy memcpy
#define __PRETTY_FUNCTION__ __FUNCDNAME__

#define __attribute__(x)
#define __attribute(x)
#define __inline__
#define inline
#endif

/* It is important that the sizes of the following data types (on the
   host) are as stated.  LibVEX_Init therefore checks these at
   startup. */

/* Always 8 bits. */
typedef  unsigned char   UChar;
typedef    signed char   Char;
typedef           char   HChar; /* signfulness depends on host */
                                /* Only to be used for printf etc 
                                   format strings */

/* Always 16 bits. */
typedef  unsigned short  UShort;
typedef    signed short  Short;

/* Always 32 bits. */
typedef  unsigned int    UInt;
typedef    signed int    Int;

/* Always 64 bits. */
typedef  unsigned long long int   ULong;
typedef    signed long long int   Long;

/* Equivalent of C's size_t type. The type is unsigned and has this
   storage requirement:
   32 bits on a 32-bit architecture
   64 bits on a 64-bit architecture. */
typedef  unsigned long SizeT;

/* Always 128 bits. */
typedef  UInt  U128[4];

/* Always 256 bits. */
typedef  UInt  U256[8];

/* A union for doing 128-bit vector primitives conveniently. */
typedef
   union {
      UChar  w8[16];
      UShort w16[8];
      UInt   w32[4];
      ULong  w64[2];
   }
   V128;

/* A union for doing 256-bit vector primitives conveniently. */
typedef
   union {
      UChar  w8[32];
      UShort w16[16];
      UInt   w32[8];
      ULong  w64[4];
   }
   V256;

/* Floating point. */
typedef  float   Float;    /* IEEE754 single-precision (32-bit) value */
typedef  double  Double;   /* IEEE754 double-precision (64-bit) value */

/* Bool is always 8 bits. */
typedef  unsigned char  Bool;
#define  True   ((Bool)1)
#define  False  ((Bool)0)

/* Use this to coerce the result of a C comparison to a Bool.  This is
   useful when compiling with Intel icc with ultra-paranoid
   compilation flags (-Wall). */
static inline Bool toBool ( Int x ) {
   Int r = (x == 0) ? False : True;
   return (Bool)r;
}
static inline UChar toUChar ( Int x ) {
   x &= 0xFF;
   return (UChar)x;
}
static inline HChar toHChar ( Int x ) {
   x &= 0xFF;
   return (HChar)x;
}
static inline UShort toUShort ( Int x ) {
   x &= 0xFFFF;
   return (UShort)x;
}
static inline Short toShort ( Int x ) {
   x &= 0xFFFF;
   return (Short)x;
}
static inline UInt toUInt ( Long x ) {
   x &= 0xFFFFFFFFLL;
   return (UInt)x;
}

/* 32/64 bit addresses. */
typedef  UInt      Addr32;
typedef  ULong     Addr64;

/* An address. In order to analyze 64-bit guests on 32-bit hosts, this must be
   64 bits wide. */
typedef Addr64 Addr;


/* Something which has the same size as void* on the host.  That is,
   it is 32 bits on a 32-bit host and 64 bits on a 64-bit host, and so
   it can safely be coerced to and from a pointer type on the host
   machine. */
#ifdef _WIN64
typedef  unsigned long long HWord;
#else
typedef  unsigned long HWord;
#endif

/* Set up VEX_HOST_WORDSIZE and VEX_REGPARM. */
#undef VEX_HOST_WORDSIZE
#undef VEX_REGPARM

/* The following 4 work OK for Linux. */
#if defined(__x86_64__) || defined(_WIN64)
#   define VEX_HOST_WORDSIZE 8
#   define VEX_REGPARM(_n) /* */

#elif defined(__i386__)
#   define VEX_HOST_WORDSIZE 4
#   define VEX_REGPARM(_n) __attribute__((regparm(_n)))

#elif defined(_WIN32) && !defined(_WIN64)
#   define VEX_HOST_WORDSIZE 4
#   define VEX_REGPARM(_n) /* ought to be __fastcall */

#elif defined(__powerpc__) && defined(__powerpc64__)
#   define VEX_HOST_WORDSIZE 8
#   define VEX_REGPARM(_n) /* */

#elif defined(__powerpc__) && !defined(__powerpc64__)
#   define VEX_HOST_WORDSIZE 4
#   define VEX_REGPARM(_n) /* */

#elif defined(__arm__) && !defined(__aarch64__)
#   define VEX_HOST_WORDSIZE 4
#   define VEX_REGPARM(_n) /* */

#elif defined(__aarch64__) && !defined(__arm__)
#   define VEX_HOST_WORDSIZE 8
#   define VEX_REGPARM(_n) /* */

#elif defined(__s390x__)
#   define VEX_HOST_WORDSIZE 8
#   define VEX_REGPARM(_n) /* */

#elif defined(__mips__) && (__mips == 64)
#   define VEX_HOST_WORDSIZE 8
#   define VEX_REGPARM(_n) /* */

#elif defined(__mips__) && (__mips != 64)
#   define VEX_HOST_WORDSIZE 4
#   define VEX_REGPARM(_n) /* */

#elif defined(__tilegx__)
#   define VEX_HOST_WORDSIZE 8
#   define VEX_REGPARM(_n) /* */

#else
#   error "Vex: Fatal: Can't establish the host architecture"
#endif


#endif /* ndef __LIBVEX_BASICTYPES_H */

/*---------------------------------------------------------------*/
/*---                                     libvex_basictypes.h ---*/
/*---------------------------------------------------------------*/

